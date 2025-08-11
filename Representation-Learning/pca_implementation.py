"""
Given a n-dimensional numpy array, the PCA implementation will identify
the prinicipal components and return the representative and coefficients

PCA is especially useful if your bases are not orthogonal. PCA will orthogonalize
the bases of your dataset.
"""
import numpy as np

class ath_PCA():
    def __init__(self):
        pass

    def do_PCA(self, input_array):
        '''
        Given an array, the function returns the representative and coefficients
        that define the dataset.
        '''
        
        # Mean centering
        centered_array = self.mean_center_data(input_array)

        # Covariance matrix
        cov = np.matmul(centered_array.transpose * centered_array)

        # Eigenvalues and eigenvectors of Covariance Matrix
        eig_val, eig_vect = np.linalg.eig(cov)

        # Note that the eigen vectors of the covariance matrix
        # represent the orthogonal principal components of a dataset
        representatives = eig_vect

        # coefiicients

        return representatives
    
    def mean_center_data(self, input_array):
        '''
        Given any array, this function calculated the mean along the zeroth
        axis and subracts it from the array. This essentially centers the data.

        The expected input is 2D however any number of dimensions would 
        technically work.
        '''
        array_means = input_array.mean(axis=0)
        output_array = input_array - array_means
        return output_array


    def kernelize(self, ):
        return
        


if __name__ == "__main__":

    input_array = np.random.randint(10, 200, size=(100, 5), dtype=int)

    pca = ath_PCA()
    pca.do_PCA()

    print("PCA Done")