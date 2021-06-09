import scipy.io
# Load data and save
gain_a = scipy.io.loadmat('gain_a.mat')
gain_b = scipy.io.loadmat('gain_b.mat')
gain_a= gain_a['gain_a']
gain_b = gain_b['gain_b']
# repeat for channel B
gainhw_a = scipy.io.loadmat('gainhw_a.mat')
gainhw_b = scipy.io.loadmat('gainhw_b.mat')
gainhw_a= gainhw_a['gainhw_a']
gainhw_b = gainhw_b['gainhw_b']
