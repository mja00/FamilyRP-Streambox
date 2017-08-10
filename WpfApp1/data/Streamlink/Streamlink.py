import sys, os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Dependencies'))
if not path in sys.path:
    sys.path.insert(1, path)
if __name__ == '__main__':
    from streamlink_cli.main import main
    main()