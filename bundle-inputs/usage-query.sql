-- Usage rows for the build (7c17e583) and fix (61226489) subagent sessions
-- of news-image-20261117. Rows appear only AFTER each session ends.
-- Parent session 1de10b8f-1185-4ebf-8021-73ffc068891b predates the
-- competition opening and is NOT bundled (bundle with --no-discover
-- --session <each session> only).
SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, u.created_at AS created_at FROM agent.agent_message_token_usage u WHERE u.agent_id IN ('7c17e583-b3ba-4a86-a614-342dc98ff67b', '61226489-82e3-4389-9969-7a8899e4a520') ORDER BY u.created_at ASC
