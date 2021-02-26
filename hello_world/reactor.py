from reactors.runtime import Reactor


def main():
    r = Reactor()
    r.logger.info("Actor received message: {}".format(r.context['raw_message']))
    r.logger.debug("This is a DEBUG message from actor {}".format(r.uid))
    r.logger.info("This is an INFO message from actor {}".format(r.uid))
    r.logger.warning("This is a warning from actor {}".format(r.uid))
    r.logger.info("Here's that secret value: {}".format(r.context.dont_reveal))
    r.logger.info("Here's that value from the config.yml: {}".format(
        r.settings.do_reveal))


if __name__ == '__main__':
    main()
