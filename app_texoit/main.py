import argparse
import unittest
from app_texoit.test.test import TestDB
from app_texoit.test.test import TestApi
from app_texoit.utils import logger
from app_texoit import create_app
from app_texoit.utils import load_data
from app_texoit.utils import create_tables
from app_texoit.utils import drop_tables





def suite_api():
    suite = unittest.TestSuite()
    suite.addTest(TestApi('test_create_movie'))
    suite.addTest(TestApi('test_read_movies'))
    suite.addTest(TestApi('test_update_movie'))
    suite.addTest(TestApi('test_patch_movie_year'))
    suite.addTest(TestApi('test_patch_movie_title'))
    suite.addTest(TestApi('test_patch_movie_studios'))
    suite.addTest(TestApi('test_patch_movie_producers'))
    suite.addTest(TestApi('test_patch_movie_winner'))
    suite.addTest(TestApi('test_delete_movie'))
    suite.addTest(TestApi('test_main_task_max'))
    suite.addTest(TestApi('test_main_task_min'))
    return suite


def suite_db():
    suite = unittest.TestSuite()
    suite.addTest(TestDB('test_load_data'))
    return suite


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--execute", type=str, required=True,
                        help="Escolhe um programa para executar das siguintes opções: scraper, api, test_api, test_scraper")
    args = parser.parse_args()

    if args.execute == 'test_db':
        logger.info('STARTING TESTING DB')
        runner = unittest.TextTestRunner()
        runner.run(suite_db())
    elif args.execute == 'test_api':
        # run test
        logger.info("STARTING TESTING API")
        runner = unittest.TextTestRunner()
        runner.run(suite_api())
    elif args.execute == "run_api":
        app = create_app()
        drop_tables(app)
        create_tables(app)
        load_data(app)
        app.run(debug=True, port=7000, threaded=True, )