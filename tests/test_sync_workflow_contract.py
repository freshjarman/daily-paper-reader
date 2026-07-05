from pathlib import Path


SYNC_WORKFLOW = Path(".github/workflows/sync.yml")


def test_sync_workflow_supports_scheduled_and_manual():
    """本 fork 需要全自动同步：定时与手动触发都要支持。"""
    text = SYNC_WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text, "sync.yml should still support manual dispatch"
    assert "schedule:" in text, "this fork intentionally keeps automatic scheduled sync"
    assert "cron:" in text, "scheduled sync requires a cron trigger"


def test_sync_workflow_pushes_with_pat_for_workflow_files():
    """GITHUB_TOKEN 无法推送 .github/workflows/** 的改动，必须用 SYNC_PAT（回退 GITHUB_TOKEN）。"""
    text = SYNC_WORKFLOW.read_text(encoding="utf-8")

    assert "secrets.SYNC_PAT" in text, (
        "checkout/push must use SYNC_PAT so upstream workflow-file changes can be synced"
    )
