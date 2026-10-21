def review(config):
    merge = config['merge']
    branch_target = merge['branch']['target']
    branch_source = merge['branch']['source']

    comments = []

    for rule in config['data']:
        message = rule['message'].replace("${BRANCH_TARGET}", branch_target)
        tp_rule = rule.get('type', 'SOURCE_TARGET_EQUALITY')

        if tp_rule == "SOURCE_TARGET_EQUALITY":
            if branch_target != branch_source:
                comments.append(__create_comment(
                    rule=rule,
                    config=config,
                    tp_rule=tp_rule,
                    message=message,
                ))
            continue

        if tp_rule == "TARGET_DENY_LIST":
            deny_list = rule['denyList']

            if branch_target in deny_list:
                comments.append(__create_comment(
                    rule=rule,
                    config=config,
                    tp_rule=tp_rule,
                    message=message,
                ))
            continue

    return comments


def __create_comment(rule, config, tp_rule, message):
    comment = {
        "id": tp_rule,
        "comment": message,
    }
    processor_args = rule.get('processorArgs', config.get('processorArgs'))

    if processor_args is not None:
        comment['processorArgs'] = processor_args

    return comment
