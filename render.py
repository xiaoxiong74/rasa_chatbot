import os

from jinja2 import Template


def render(input_file, output_file):

    with open(input_file, encoding='utf_8') as input_fd, open(output_file, mode='w', encoding='utf_8') as output_fd:
        template = Template(input_fd.read())

        action_endpoint_url = os.environ.get('ACTION_ENDPOINT_URL', "http://192.168.109.232:5055/webhook")
        print("action will connect to {}".format(action_endpoint_url))

        nlu_url = os.environ.get('NLU_URL', "http://192.168.109.232:5000")
        print("nlu will connect to {}".format(nlu_url))

        rendered_string = template.render(action_endpoint_url=action_endpoint_url, nlu_url=nlu_url)

        output_fd.write(rendered_string)


if __name__ == "__main__":
    render('endpoints.yml.tpl', 'endpoints.yml')
