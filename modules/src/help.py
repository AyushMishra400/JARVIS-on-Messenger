from templates.text import TextTemplate

def process(input, entities=None):
    help = 'Hi there! I\'m Jarvis, your personal assistant.'
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            help = help.replace('there', sender_name)
    help += '\nTell me things like:'
    help += '\n  - define comfort'
    help += '\n  - iron man 2 movie plot'
    help += '\n  - tell me a joke/quote/fact'
    help += '\n  - wiki html'
    help += '\n  - anything you want book'
    help += '\n  - usd to eur rate'
    help += '\n  - death note anime'
    help += '\n  - time in seattle'
    help += '\n  - songs by linkin park'
    help += '\n  - shorten google.com'
    help += '\n  - weather in london'
    help += '\n  - videos of sia'
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
