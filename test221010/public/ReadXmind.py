#xmind文件读取
import time

import pandas as pd
import xmindparser
import zipimport

#xmindzip = 1
def xmind_read(xmind_file=r"C:\Users\zhouwei\Documents\主题readtest.xmind"):
    #读取xmind文件里所有画布内容
    xmind_data=xmindparser.xmind_to_dict(xmind_file)
    draw_num=len(xmind_data)
    print(f"思维导图里有{draw_num}张画布")
    return xmind_data


#将每个topic的详细信息处理成最终写入Excel用例文件的dict格式
def process_topic(topicmsg):
    '''
    :param topicmsg: xmind最末尾的分支，即topic信息
    :return: topicdata,写入Excel的每个用例
    '''
    topicdata = {'用例标题': '', '优先级': '2', '前提': None, '步骤': None,"结果":None}
    try:

        newtitle= topicmsg['title']
        # 只有2层主题会出现两个重复的一级主题处理
        if newtitle.find("/")!=-1:
            nts=newtitle.split("/")
            if nts[0]==nts[1]:
                nts.pop(0)
                newtitle="/".join(nts)
        topicdata["用例标题"] = newtitle

        #4层主题会出现丢失的第二层主题名称怎么处理

        if "makers" in topicmsg.keys():
            topicdata["优先级"] = topicmsg['makers'][0][-1]
        # 首先拿到输入的索引值
        put_index=topicmsg['note'].index("\n输入")
        out_index=topicmsg['note'].index("\n输出")
        print(topicmsg['note'].index("\n输入"))

        # print(a['note'][0]+a['note'][1])
        # 字符串切片取出前提内容, 取出前提，输入和输出放在一起
        #如果找不到前提，就拿note的所有值
        print(topicmsg['note'][0:put_index:1])
        topicdata["前提"] = topicmsg['note'][0:put_index:1]
        putandresult=topicmsg['note']
        topicdata["步骤"] = topicmsg['note'][put_index+1:out_index:]
        topicdata["结果"] = topicmsg['note'][out_index::]
        # if topicdata["前提"] is not None:
        #     print("输入和结果是默认的值")
        #     topicdata["输入以及结果"]=putandresult

        #print("存在的索引值", topicmsg['note'].find("\n输入"))
    except Exception as e:
        print("获取该用例内容出现错误")
        print(e)
    # else:
    #     topicdata["用例标题"]=topicmsg['title']
    return topicdata

f_topicnames=[]
first_titlename=[]

topicdatas=[]
topicnotes=[]
def foreach_topic(son_topic,tt):
    #numberone='分支主题A/A 1'
    ftpnames=[]
    cunt_call=0
    intopic=1

    print("共有{}层".format(intopic))
    f_topicname = son_topic["title"]
    ftpnames.append(f_topicname)
    print("方法内累积title名："+f_topicname+".")
    for s_topic in son_topic["topics"]:
        print("一层循环内累积title名：" + s_topic["title"])

        print("这是子分支下的详细信息")
        print(s_topic)
        if "topics" in s_topic.keys():
            print(s_topic["title"]+"  的子分支下还有子分支")
            foreach_topic(s_topic,tt)
            intopic+=1
            print("共有{}层".format(intopic))

        else:
            cunt_call+=1
            print(f"分支的数量是{cunt_call+intopic}")
            print(s_topic["title"]+"  这个子分支下没有分支了")
            s_topicname=s_topic["title"]
            #tname=f_topicname.join("/",s_topicname)
            tname="/".join([tt,f_topicname,s_topicname])
            print("最终的title名："+tname)
            f_topicnames.append(tname)
            s_topic["title"]=tname
            print("循环内的topic信息：",s_topic)
            if "note"  in s_topic.keys():
                topicnote=s_topic["note"]
                topicnotes.append(topicnote)
            else:
                print("分支下没有备注，默认无备注")
                s_topic["note"]="无备注"
                topicnotes.append(s_topic["note"])
            topicdatas.append(process_topic(topicmsg=s_topic))


    

    
stitles=[]
compose_titles=[]
def get_titles(data,topic_title=1):
    #先获取第1级分支主题有多少
    father_count=0
    son_count=0
    firstcount=0
    for num in data:
        #第一层循环，主要是画布总体内容
        print("下面是画布的内容")
        print(num)
        #第二层循环，画布单主题下的一级分支

        for i in num["topic"]["topics"]:
            #第一个分支的title名
            ftitle=i["title"]
            first_titlename.append(ftitle)
            father_count+=1
            #这里可以再做个二层循环，把第二层的title取出来
            try:
                for si in i["topics"]:
                    stitle=si["title"]
                    stitles.append(stitle)
                    print("二层循环里面的title集合：", si)
                    fst=ftitle+"/"+stitle
                    print(fst)
                    compose_titles.append(ftitle+"/"+stitle)
            except Exception as e:
                print(e)

            try:
                print(father_count)
                print("开始输出一级分支里的topic")
                print(i)
                #第三层循环，如果一级分支下还有子集分支，继续取子集分支下的topics
                
                
                # for u in i["topics"]:
                    # print("开始输出子集分支topics下面含有的topics")
                    # print(u)
                    # son_count+=1
                    
                #使用方法调用
                foreach_topic(son_topic=i,tt=ftitle)
                    
                # if i is not None:
                    # print("这是非空分支")
                    # if i["topic"]["topics"] is not None:
                        # print("分支下面还有分支")
                        # for n in i["topic"]["topics"]:
                            # son_count+=1
                    # else:
                        # print("此分支下没有分支了")
                    
                # else:
                    # print("该分支下没有子分支")
                
            except Exception as e:
                #下面没有分支的，取出来放好
                f_topicnames.append(ftitle)

                topicdatas.append(process_topic(i))
                if "note" in i.keys():
                    topicnote = i["note"]
                    topicnotes.append(topicnote)
                else:
                    print("分支下没有备注，默认无备注")
                    i["note"] = "无备注"
                    topicnotes.append(i["note"])
                #topicnotes.append(i["note"])
                father_count+=1
                print("出错了")
                
                print(e)
            else:
                print(father_count)
        #father_count+=1
    
    print(son_count)
    print("这是分支下的子分支数")  
    print(father_count)
    

def get_topics(data,topic_titles):
    pass
    

if __name__ == '__main__':
   time_start=time.perf_counter()
   #主题readtest
   x=xmindparser.xmind_to_dict(r"C:\Users\zhouwei\Documents\主题readtest.xmind")
   print("输出读取的xmind内容")
   print(type(x))
   print(x)
   print("下面遍历输出xmind读取的内容")
   print("画布名：",x[0]["title"])
   for i in x:
       print("下面打印主题的详细")
       tps=i["topic"]["topics"]
       print(tps) 
       for tp in range(0,len(tps)):
            print("开始打印子主题：第 "+str(tp)+" 个")
            print("标题名：",tps[tp]["title"])
            print(tps[tp])
    
   try:
        x_df=pd.DataFrame(x)
   except Exception as e:
        print("出现错了，下面是错误信息")
        print(e)
   print("下面输出x_df，DataFrame内容")
   print(x_df)
   print("读取xmind成功！！！")
   get_titles(data=x,topic_title=1)
   print(f_topicnames)
   print(first_titlename)
   print(stitles)
   print(compose_titles)
   print("尝试把用例写进Excel")
   '''a={'title': 'C1', 'note': '前提：\n这是c的前提\n输入：\n这是c的备注\n输出：\n这是c的备注', 'makers': ['priority-7']}
   a_bak={}
   for a_item in a.items():
       a_bak["用例标题"]=a['title']
       a_bak["优先级"]=a['makers'][0][-1]
       #取出前提，输入和输出放在一起
       #首先拿到输入的索引值
       print(a['note'].index("\n输入"))
       #print(a['note'][0]+a['note'][1])
       #字符串切片取出前提内容
       print(a['note'][4:10:1])
       a_bak["前提"]=a['note'][3:10:1]
       a_bak["输入以及结果"]=a['note'][11::]
       print(a_item)'''

   #pd.DataFrame(topicdatas).to_excel("./cases.xlsx",index=False)
   print("xmind转Excel用例成功")
   print(topicdatas)
   print(topicnotes)
   #前提这一列没有的，note备注全放在 输入以及结果
   for tdi in range(0,len(topicdatas)):
       if topicdatas[tdi]["前提"] == None or topicdatas[tdi]["前提"]=="":
           topicdatas[tdi]["结果"] = topicnotes[tdi]
           # a="abcd"
           # print(a.__len__())

    #topicdatas[tdi]["输入以及结果"]=topicnotes[tdi]
   print(topicdatas)
   #process_topic()
   pd.DataFrame(topicdatas).to_excel("./cases.xlsx", index=False)
   print(time.ctime())
   print(type(time.ctime()))
   time_end = time.perf_counter()
   run_time = time_end - time_start
   print("运行时长：", run_time)
   