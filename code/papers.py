import pandas as pd

papers = pd.read_csv('Papers.csv')
form = pd.read_csv('form.csv')
#print (papers['Paper ID'][2])
index = form.index
condition = lambda pid :form['Please provide your paper ID.'] == pid
for i , pid in enumerate (papers['Paper ID']):
    if (condition(pid).any()):
        index_c = index[condition(pid)]
        title = papers['Paper Title'][index_c[0]]
        authors = form['Please provide the author names in the order you want them to appear on the website.'][index_c[0]]
        print("<tr> <td> <b>{}</b>(<a href=\"files/{}.pdf\">pdf</a>)</td> <td>{}</td> </tr>".format(title, pid, authors))
    else:

        title = papers['Paper Title'][i]
        authors = papers['Author Names'][i]
        print("<tr> <td> <b>{}</b>(<a href=\"files/{}.pdf\">pdf</a>)</td> <td>{}</td> </tr>".format(title, pid, authors))

#      <tr> <td> <b>Federated Learning's Blessing: FedAvg has Linear Speedup </b>(<a href="files/1.pdf">pdf</a>)</td> <td>Zhaonan Qu, Kaixiang Lin, Zhaojian Li, Jiayu Zhou</td> </tr>
    
