def review(config):
    message = config['data'][0]['message']

    merge = config['merge']
    branch_target = merge['branch']['target']
    branch_source = merge['branch']['source']

    comments = []

    if branch_target != branch_source:
        comments.append({
            "id": "_",
            "comment": message
        })

    return comments
