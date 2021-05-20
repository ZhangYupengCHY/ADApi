import os

tableName = 'high_quality_keywords'

ret = os.popen(
    f"sqlacodegen --noviews --noconstraints --noindexes --tables {tableName} mysql://marmot:marmot123@wuhan.yibai-it.com:33061/server_camp_report?charset=utf8"
)
print(ret.read())