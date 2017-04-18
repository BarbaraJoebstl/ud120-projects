def doPCA():
    from sklearn.decomposition import PCS
    pca = PCA(n_components=2)
    pca.fit(data)
    return pca

pca = doPCA()
print pca.explained_variance_ration_
first_px = pca.components_[0]
second_pc = pca.components_[1]

transformed_data = pca.transform(data)
for ii, jj in zip(transformed_data, data):
    plt.scatter(first_pc[0]*ii[0], first_pc[1]*ii[0], color="r")
        plt.scatter(first_pc[0]*ii[1], first_pc[1]*ii[1], color="c")
        plt.scatter(jj[0], jj[1], color="b")
plt.xlabel("bonus")
plt.ylabe("long-term incentive")
plt.show()        
