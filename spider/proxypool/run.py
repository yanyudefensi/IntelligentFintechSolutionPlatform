from proxypool import scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = scheduler.Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
