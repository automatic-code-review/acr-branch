def review(config):
    merge = config['merge']
    branch_target = merge['branch']['target']
    branch_source = merge['branch']['source']

    comments = []

    for rule in config['data']:
        message = rule['message'].replace("${BRANCH_TARGET}", branch_target)
        tp_rule = rule.get('type', 'EQUALITY')

        if tp_rule == "SOURCE_TARGET_EQUALITY":
            if branch_target != branch_source:
                comments.append({
                    "id": tp_rule,
                    "comment": message
                })
            continue

        if tp_rule == "TARGET_DENY_LIST":
            deny_list = rule['denyList']

            if branch_target in deny_list:
                comments.append({
                    "id": tp_rule,
                    "comment": message
                })
            continue

    return comments
