from crhelper import CfnResource

helper = CfnResource()


@helper.create
@helper.update
def make_thing_lowercase(event, _):
    s = str(event["ResouceProperties"]["data"]).lower()
    helper.Data["Result"] = s


@helper.delete
def no_op(_, __):
    pass


def handler(event, context):
    helper(event, context)
