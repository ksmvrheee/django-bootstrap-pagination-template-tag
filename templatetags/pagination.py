from django import template


register = template.Library()


@register.inclusion_tag('pagination.html', takes_context=True)
def create_pagination(context, current_page_number: int,
                      pages_count: int) -> dict[str, None | str | list[int]]:
    """
    Creates pagination for a page.
    Gets two arguments: the number of the current page
    and the number of pages available.

    :param context: general page context.
    :param current_page_number: the number of the current page.
    :param pages_count: the number of pages available.
    :return: a context for the subtemplate representing
    an info about pages to display.
    """
    query_string = '?'

    for param, value in context['request'].GET.items():
        if param != 'page':
            query_string += f'{param}={value}&'

    pagination_context = {
        'current_page_number': current_page_number,
        'previous_page': None,
        'next_page':  None,
        'query_string': query_string
    }

    if pages_count > 1:
        previous_pages_count = current_page_number - 1
        next_pages_count = pages_count - current_page_number
        has_previous = bool(previous_pages_count)
        has_next = bool(next_pages_count)

        pagination_queue = []

        if not has_previous:
            if next_pages_count >= 2:
                pagination_context["next_page"] = current_page_number + 1
                pagination_queue += [
                    current_page_number,
                    current_page_number + 1,
                    current_page_number + 2,
                ]

            else:
                pagination_context["next_page"] = current_page_number + 1
                pagination_queue += [
                    current_page_number,
                    current_page_number + 1,
                ]

        else:
            pagination_context["previous_page"] = current_page_number - 1

            if not has_next:
                if previous_pages_count >= 2:
                    pagination_queue += [
                        current_page_number - 2,
                        current_page_number - 1,
                        current_page_number
                    ]

                else:
                    pagination_queue += [
                        current_page_number - 1,
                        current_page_number
                    ]

            else:
                pagination_context["next_page"] = current_page_number + 1
                pagination_queue += [
                    current_page_number - 1,
                    current_page_number,
                    current_page_number + 1,
                ]

        pagination_context["pages"] = pagination_queue

    return pagination_context
