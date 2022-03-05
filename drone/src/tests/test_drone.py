#!/usr/bin/env python
# coding=utf-8
import pytest


@pytest.mark.parametrize(
    "area, route",
    [
        #
        (
            (6, 3),
            [[(0, 0), (2, 1), (4, 0), (6, 1)], [(5, 3), (3, 2), (1, 3), (-1, 2)]],
        ),
    ],
)
def test_run(
    mocker,
    area,
    route,
):
    """
    test the whole process, incl. search, bugzilla_process, review
    """

    mocker.patch(
        "auto_submit.error_handling_service.models.search.pre_search.single_search",
        return_value=242494,
    )
    mocker.patch(
        "auto_submit.error_handling_service.models.do_job.get_bzapi", return_value=bzapi
    )
    mocker.patch(
        "auto_submit.error_handling_service.models.review.review._request_testcase_history_page"
    )

    df_testcase = pd.DataFrame(testcase_info, index=[0])
    path = (
        testcase_info["CRASH_DUMP"]
        if testcase_info["ERROR_TYPE"] == "crash"
        else testcase_info["TRACE_LINK"]
    )

    if path:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        mocker.patch.object(CrashDump, "fetch_text_from_file", return_value=text)
        mocker.patch.object(SingleTest, "fetch_text_from_file", return_value=text)

    res = execute_service(
        QADB,
        df_testcase,
        is_breakage_issue=True,
    )
    assert res == expected
