from django import template


register = template.Library()

@register.filter(name='sort_votes')
def listsort(value):
    return sorted(value, key=lambda x: -x.votes)
