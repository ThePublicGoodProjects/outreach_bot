wget http://bit.ly/miniconda -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set show_channel_urls true
conda update conda
conda update --all
conda config --add channels conda-forge --force
git clone https://github.com/ThePublicGoodProjects/outreach_bot.git
cd outreach_bot
conda create --name TWITTER python=3 --file requirements.txt
source activate TWITTER
conda info --all
conda list