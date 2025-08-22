from .pipeline import main
if __name__ == '__main__':
    import sys
    main(sys.argv[1] if len(sys.argv)>1 else 'modules/vision/config/oal_counter.yaml')
