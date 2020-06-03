# %%
import os
import sys
from PIL import Image

def compressMe(folder, file, verbose=False, quality=85):
	filepath = os.path.join(folder, file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath).convert(mode='RGB')
	dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	picture.save(os.path.join(folder, "Compressed_"+file),"jpeg",optimize=True,quality=quality) 
	
	newsize = os.stat(os.path.join(folder,"Compressed_"+file)).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	if (verbose):
		print("File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent))
	return percent

# %%
os.chdir(os.path.expanduser('~/Documents/OneDrive/Northwestern/Study/Courses/Concept_Drift/paper_draft/cd_paper'))

# %%
ls_folders_files = [('./figures/v14/credit_default/logi_scal_PI_train_sample_weights/', 'pos_single_credit_mlines_with_regu_1e-08_0_0001_0_001_99_0.png'),
                    ('./figures/v14/credit_default/logi_scal_PI_train_sample_weights/', 'pos_single_credit_fisher_mlines_with_regu_1e-08_0_0001_0_001_99_0.png'),
                    ('./figures/v14/bike_sharing/reg_lin_A/quadr/', 'PII_pos_single_retro_bike_fisher_mlines_with_regu_1e-08_0_0001_0_01_99_99.png'),
                    ('./figures/v14/bike_sharing/reg_lin_B_1/quadr/', 'PII_pos_single_retro_bike_fisher_mlines_with_regu_1e-08_0_0001_0_01_99_99.png'),
                    ('./figures/v14/bike_sharing/reg_lin_C/quadr/', 'PII_pos_single_retro_bike_fisher_mlines_with_regu_1e-08_0_0001_0_01_99_99.png'),
                    ('./figures/v14/bike_sharing/reg_lin_C_2/quadr/', 'PII_pos_single_retro_bike_fisher_mlines_with_regu_1e-08_0_0001_0_01_99_99.png'),
                    ('./figures/v14/bike_sharing/reg_lin_PI_D_2/quadr/', 'pos_single_bike_fisher_mlines_with_regu_1e-08_0_0001_0_01_99_99.png')]
for folder, file in ls_folders_files:
    compressMe(folder, file, verbose=True, quality=65)

# %%


# %%
