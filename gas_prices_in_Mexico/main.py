from get_data import make_data_file
from clean_data import clean_data
from make_dashboard import run_dash_app

N_RESULTS = 5000

if __name__ == "__main__":
    make_data_file(5000)
    clean_data()
    run_dash_app(host="0.0.0.0", port=9000, debug=True)
