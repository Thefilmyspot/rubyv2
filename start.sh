if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/abhinand2608/anadearmas
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /abhinand2608/anadearmas
fi
cd /anadearmas
pip3 install -U -r requirements.txt
echo "Starting anadearmas ...."
python3 bot.py
