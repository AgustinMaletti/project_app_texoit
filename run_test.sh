DIR="venv"
if [ -d "$DIR" ]; then
# Take action if $DIR exists. #
echo "Allready exist dir ${DIR}..."
source venv/bin/activate
pip install -r requirements.txt
else
  echo "creating venv ${DIR}..."
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi
python -m app_texoit.main -e test_api