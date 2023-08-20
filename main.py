import glob
import os
import json
import pandas as pd
import numpy

os.chdir("./")
files = []
for file in glob.glob("*.json"):
    files.append(file)

print(files)


#
# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(columns=['name', 'city', 'state',
                  'nirfRank', 'rank'])


# print dataframe.
df

for j in files:
    f = open(j)
    data = json.load(f)

    for i in data:
        if ("name" in i):
            new_row = pd.Series({
                'name': str(i.get("name", numpy.NaN)),
                'city': str(i.get("city", numpy.NaN)),
                'state': str(i.get("state", numpy.NaN)),
                'nirfRank': str(i.get("nirfRank",   numpy.NaN)),
                'rank': str(i.get("rank", numpy.NaN)),
            })
        else:
            break
        df = pd.concat([
            df,
            pd.DataFrame([new_row], columns=new_row.index)]
        ).reset_index(drop=True)

        print(i)

    f.close()

df = df.drop_duplicates(subset=["name", "city", "state"], keep="last")
# Keep rows with non-null values in "nirfRank" or "rank" columns
df = df[~(df["nirfRank"].isnull() & df["rank"].isnull())]
# Sort the DataFrame by "name"
df.sort_values("name", inplace=True)
# Reset index
df.reset_index(drop=True, inplace=True)
# Save the result to a CSV file
df.to_csv('college_filtered.csv', index=False)

# df.to_csv('data.csv')


# df.reset_index(drop=True, inplace=True)
# df.to_csv('course_filtered.csv')

# # sorting by first name
# df.sort_values("name", inplace=True)

# # # dropping ALL duplicate values
# # df.drop_duplicates(subset="name",
# #                    keep="last", inplace=True)

# df.reset_index(drop=True, inplace=True)

# # df = df.drop(df.columns[[0, 4, 5, 6, 7]], axis=1)

# df.sort_values("name", inplace=True)

# df.to_csv('college_nigga.csv')

# text_file = open("college.txt", "w")

# df = pd.read_csv('college_dataset_1.csv')
# for index, row in df.iterrows():

#     text_file.write('<option value="' + row['name'] + '">' + '</option>\n')
#     # text_file.write('<option value="' + row['name'] +'">' + str(row['city']) + ", " + str(row['state']) + '</option>\n')

# text_file.close()


# 3

# os.chdir("./")
# tx_fil = []
# for file in glob.glob("*.txt"):
#     tx_fil.append(file)


# df = pd.DataFrame(columns=['course'])

# for fil in tx_fil:
#     text_file = open(fil, "r")

#     data = []
#     d = []
#     for i in text_file:
#         # print(i,i.find('title="'))
#         for j in range(len(i)):
#             try:
#                 if i[j]+i[j+1]+i[j+2]+i[j+3]+i[j+4]+i[j+5]+i[j+6] == 'title="':
#                     short_text = i[j+7:]
#                     tt = short_text
#                     for k in range(len(short_text)):
#                         if short_text[k] + short_text[k+1] == '">':
#                             tt = short_text[:k]
#                             d.append(tt)
#                     break
#             except:
#                 pass
#     for f in d:
#         for h in range(len(f)):
#             try:
#                 if f[h]+ f[h+1]+ f[h+2]+ f[h+3]+ f[h+4]+ f[h+5]== "&nbsp;":
#                     print("2", f[:h])
#                     data.append(f[:h])
#                     break
#                 if f[h]== ";":
#                     print("3", f[:h])
#                     data.append(f[:h])
#                     break
#             except:
#                 pass


#     for i in d:
#         print(i)
#         new_row = pd.Series({
#                 'course':str(i),
#             })
#         df =  pd.concat([
#                 df,
#                 pd.DataFrame([new_row], columns=new_row.index)]
#            ).reset_index(drop=True)

# df.sort_values("course", inplace=True)

# df.drop_duplicates(subset="course",
#                       keep="last", inplace=True)
# print(df)

# df.to_csv('course_data.csv')


# text_file.close()

# text_file = open("course_details", "w")
# df = pd.read_csv('course_data.csv')
# for index, row in df.iterrows():

#     text_file.write('<option value="' + row['course'] +'">'+ '</option>\n')
#     #text_file.write('<option value="' + row['name'] +'">' + str(row['city']) + ", " + str(row['state']) + '</option>\n')

# text_file.close()


"""
special tx to 
https://www.indiacollegeshub.com/courses/ug-courses-india.aspx
&
https://github.com/Clueless-Community/collegeAPI
"""
