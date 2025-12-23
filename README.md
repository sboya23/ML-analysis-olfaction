## 🐭 Scripts for processing and statistical analysis of ML pipeline using DeepLabCut and SimBA to analyse olfaction task in mice 

>
>Download scripts and data files.

>
>After extracting the Data folder change the working directory in each .py or .rmd file to the correct one for you.

>
>Run .rmd analysis files within each folder, clean RStudio workspace in-between scripts.

## Contents

* **DLC and video data prep for SimBA analysis** - contains scripts for removing cotton bud frames from videos and matching the DLC tracking files to the cleaned up videos. Video and DLC prep folder contains .py script that removes video frames without cotton bud based on DLC confidence scores - you need to have your video files and DLC output in the same folder with matching ids, together with the script file, adjust the column location for the cotton bud data based on your set up. DLC prep contain a single example DLC output file and a script to filtered out data for frames without cotton bud and to remove cage output afterwards.
 
* **Figure 3** - contains 5x .csv files, C9orf72 study - 1) young, and 2) old time point correlation data showing time binned data for sniffing time at every cotton bud presentation from manual and ML scoring, Tardbp study - 3) young, and 4) old time point correlation data showing time binned data for sniffing time at every cotton bud presentation from manual and ML scoring, 5) data for correlation analysis from two manual scorers; 2x .rmd files 1) correlation.rmd for analysis of manual vs ML scoring, 2) correlation_manual2.rmd - for analysis of correlation between two manual scorers.


* **Figure 4** - contains 4x .csv files - C9_all.csv contains all datasets - young and old time points - manual and ML - filtered and non-filtered (for the 10s threshold) from the C9orf72 study, TDP-all.csv contains all datasets - young and old time points - manual and ML - filtered and non-filtered (for the 10s threshold) from the Tardbp study, used to plot histograms of filtering of the manual and ML datasets. C9_nonfiltered_status.csv and TDP_nonfiltered_status.csv contains manual and ML non-filtered data with additional column showing the status of each datapoint - if it would be filtered or not, according to the 10s threshold for the C9orf72 and Tardbp study. The histograms.rmd file contains scripts to plot histograms of filtering status for the C9orf72 and Tardbp study, as well as glmer and anova statistical comparison of how many points are filtered from the manual vs ML datasets.

* **Figure 5** - contains 4x .csv files and 4x .rmd files. The .csv files show data filtered for under 10 s sniffing trials on the first odour presentation from the C9orf72 study - 1) young, and 2) old time point, Tardbp study - 3) young, and 4) old time point. The .rmd files contain scripts for lmer and anova statistical analysis of the data from the C9orf72 study - 5) young, and 6) old time point, Tardbp study - 7) young, and 8) old time point.

* **Simba training** - contains features importance logs, classification reports, learning cures and meta data files for the Simba model that was trained to analyse the validation dataset present in the paper.

* **Simba output - 1 second time bins** - Time_bins_ML_reslts.csv shows the raw output from the Simba validation analysis of unseen videos of estimated time spent sniffing at every 1 s time bin from each validation video. time_binning_9.py compiles these 1 s time bins into 9 values - one for each cotton bud presentation according to the duration of each individual video.

* **Manual scores** - all manual scores.zip folder contains all manual scores from each video used in the validation analysis presented in the paper, including .py scripts for collating individual files together.

  Analysis pipeline:

<img width="1090" height="597" alt="schematic" src="https://github.com/user-attachments/assets/def78109-fd1a-4af6-b20f-52958aacdb8b" />

