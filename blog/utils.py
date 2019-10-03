from django.utils.text import slugify


def unique_slug_generator(model_instance, title):
    """
    From tutorial: https://www.youtube.com/watch?v=hY5F3EGcff4 and modified to
    not show the id of the model_instance, just add an iterated number.
    """
    slug = slugify(title)
    model_class = model_instance.__class__
    counter = 0

    while model_class._default_manager.filter(slug=slug).exists():
        counter = counter + 1
        if counter > 1:
            slug = "-".join(slug.split('-')[:-1])
        slug = f'{slug}-{counter}'

    return slug
