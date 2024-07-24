def get_object_or_None(model, **kwargs):
    try:
        item = model.objects.get(**kwargs)
        return item
    except model.DoesNotExist:
        return None