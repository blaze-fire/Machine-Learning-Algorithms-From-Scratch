import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y) 
        n_classes = len(self._classes)

        # init, vars, priors

        self._mean = np.zeros((n_classes, n_features), dtype = np.float64 )
        self._var = np.zeros((n_classes, n_features), dtype = np.float64 )
        self._priors = np.zeros(n_classes, dtype = np.float64)

        for idx,c in enumerate(self._classes):
            X_c = X[c==y]
            self._mean[idx,:] = X_c.mean(axis=0)
            self._var[idx,:] = X_c.var(axis=0)
            self._priors[idx] = X_c.shape[0] / float(n_samples)       # frequency of class c ocurring
    


    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return y_pred

        
    def _predict(self, X):
        posteriors = []

        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            class_conditional = np.sum(np.log(self._pdf(idx,c)))
            posterior = prior + class_conditional
            posteriors.append(posterior)
            
        return  self._classes[np.argmax(posteriors)]

    
    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-(x-mean)**2 / (2*var))
        denominator = np.sqrt(2*np.pi*var)
        return numerator / denominator

