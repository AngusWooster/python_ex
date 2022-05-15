#!/usr/bin/python3


def myxml(tag, content='', **args):
    attrs_list = []
    for key, value in args.items():
        # print(f'key={key}, value={value}')
        attrs_list.append(f' {key}="{value}"')
    attrs = ''.join(attrs_list)

    return f'<{tag}{attrs}>{content}</{tag}>'

print(myxml('foo', 'bar', a=1,b=2,c=3))