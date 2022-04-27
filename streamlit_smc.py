import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import json,datetime,math
from collections import Counter

st.sidebar.header('TDS3751 - SOCIAL MEDIA COMPUTING')

aspects = ['Followers Growth Rate (Part 1)','Active Rate (Part 1)','Responsiveness (Part 1)','Engagement Rate (Part 1)','Top 5 Hashtags Used (Part 1)','Accounts That Follow More Than One Brand (Part 2)','Community Similarities (Part 2)']

question = st.sidebar.radio('Please choose an aspect to view',aspects)
cinemas = ['GSC','TGV','MMC']

############Q1############
if question == aspects[0]:

    st.header("1. Followers growth rate from 2022-03-07 to 2022-03-20")

    gsc_followers_count_data = pd.read_json('Collected_data/GSC_followers_count.json', lines=True)
    tgv_followers_count_data = pd.read_json('Collected_data/TGV_followers_count.json', lines=True)
    mmc_followers_count_data = pd.read_json('Collected_data/MMC_followers_count.json', lines=True)

    cols = st.columns(3)

    with cols[0]:
        gsc_followers_dif = gsc_followers_count_data['followers_count'].values[-1] - gsc_followers_count_data['followers_count'].values[0]
        st.success('Followers Gained (Last 14 days): '+str(gsc_followers_dif)+' (+'+str(round(gsc_followers_dif/gsc_followers_count_data['followers_count'].values[0]*100,2))+'%)')

        fig = plt.figure(figsize = (10, 6))
        plt.plot(gsc_followers_count_data['date'], gsc_followers_count_data['followers_count'])
        plt.xlabel("Date")
        plt.ylabel("Followers Count")
        plt.yticks(range(gsc_followers_count_data['followers_count'].values[0]-200,gsc_followers_count_data['followers_count'].values[0]+1200,200))
        plt.title("GSC Followers Count Over Time")
        plt.xticks(rotation ='45')
        st.pyplot(fig)
    with cols[1]:
        tgv_followers_dif = tgv_followers_count_data['followers_count'].values[-1] - tgv_followers_count_data['followers_count'].values[0]
        st.success('Followers Gained (Last 14 days): '+str(tgv_followers_dif)+' (+'+str(round(tgv_followers_dif/tgv_followers_count_data['followers_count'].values[0]*100,2))+'%)')

        fig = plt.figure(figsize = (10, 6))
        plt.plot(tgv_followers_count_data['date'], tgv_followers_count_data['followers_count'])
        plt.xlabel("Date")
        plt.ylabel("Followers Count")
        plt.yticks(range(tgv_followers_count_data['followers_count'].values[0]-200,tgv_followers_count_data['followers_count'].values[0]+1200,200))
        plt.title("TGV Followers Count Over Time")
        plt.xticks(rotation ='45')
        st.pyplot(fig)
    with cols[2]:
        mmc_followers_dif = mmc_followers_count_data['followers_count'].values[-1] - mmc_followers_count_data['followers_count'].values[0]
        st.success('Followers Gained (Last 14 days): '+str(mmc_followers_dif)+' (+'+str(round(mmc_followers_dif/mmc_followers_count_data['followers_count'].values[0]*100,2))+'%)')

        fig = plt.figure(figsize = (10, 6))
        plt.plot(mmc_followers_count_data['date'], mmc_followers_count_data['followers_count'])
        plt.xlabel("Date")
        plt.ylabel("Followers Count")
        plt.yticks(range(mmc_followers_count_data['followers_count'].values[0]-200,mmc_followers_count_data['followers_count'].values[0]+1200,200))
        plt.title("MMC Followers Count Over Time")
        plt.xticks(rotation ='45')
        st.pyplot(fig)
    st.write('The three line charts above display the followers count of GSC, TGV and MMC for a two weeks period starting from 7/3/2022. It is obvious that both GSC and TGV have an increasing followers growth rate but not MMC as the almost flat line suggested. The followers of GSC increased for 0.22% while for TGV it increased by 1.21%. Lastly for MMC, it only gained 7 more followers in a two weeks period. Overall, TGV has the highest followers growth rate among these three cinemas because it gained almost 1000 followers in two weeks.')

############Q2############
elif question == aspects[1]:

    st.header("2. Active rate")
    gsc_tweets = pd.read_json('Collected_data/GSC_tweets.json', lines=True)
    gsc_tweets['created_at'] = gsc_tweets['created_at'].dt.strftime('%d/%m/%Y')
    a = gsc_tweets.groupby("created_at").size().values
    gsc_tweets= gsc_tweets.drop_duplicates(subset="created_at").assign(tweet_count=a)
    gsc_tweets.drop(gsc_tweets.columns.difference(['created_at','tweet_count']), 1, inplace=True)
    gsc_tweets.sort_values(by=['created_at'], inplace=True)

    tgv_tweets = pd.read_json('Collected_data/TGV_tweets.json', lines=True)
    tgv_tweets['created_at'] = tgv_tweets['created_at'].dt.strftime('%d/%m/%Y')
    b = tgv_tweets.groupby("created_at").size().values
    tgv_tweets= tgv_tweets.drop_duplicates(subset="created_at").assign(tweet_count=b)
    tgv_tweets.drop(tgv_tweets.columns.difference(['created_at','tweet_count']), 1, inplace=True)
    tgv_tweets.sort_values(by=['created_at'], inplace=True)

    mmc_tweets = pd.read_json('Collected_data/MMC_tweets.json', lines=True)
    mmc_tweets['created_at'] = mmc_tweets['created_at'].dt.strftime('%d/%m/%Y')
    c = mmc_tweets.groupby("created_at").size().values
    mmc_tweets= mmc_tweets.drop_duplicates(subset="created_at").assign(tweet_count=c)
    mmc_tweets.drop(mmc_tweets.columns.difference(['created_at','tweet_count']), 1, inplace=True)
    mmc_tweets.sort_values(by=['created_at'], inplace=True)

    cols = st.columns(2)

    with cols[0]:
        fig = plt.figure(figsize = (10, 6))
        plt.plot(gsc_tweets['created_at'], gsc_tweets['tweet_count'], label='GSC')
        plt.plot(tgv_tweets['created_at'], tgv_tweets['tweet_count'], label='TGV')
        plt.plot(mmc_tweets['created_at'], mmc_tweets['tweet_count'], label='MMC')
        plt.title('Tweets Over Time')
        plt.xlabel('Date')
        plt.ylabel('Tweets Count')
        plt.xticks(rotation ='90')
        plt.legend()
        st.pyplot(fig)
    with cols[1]:
        st.write('This multiple line chart shows the number of tweets that these three cinemas posted within the two weeks period. TGV and GSC are more active compared to MMC as they can tweet at least five times to at most 40 times in one day. While for MMC, it only tweeted 5 times on 8/3/2022 and 19/3/2022. For the other days, it tweeted less than 5 times or did not post any tweets at all. ')

############Q3############
elif question == aspects[2]:

    st.header("3. Responsiveness")

    avg_response_time = []
    reply_count_list = []

    for cinema in cinemas:
        filename_cinema = 'Collected_data/'+cinema+'_tweets.json'
        filename_user = 'Collected_data/'+cinema+'_user_tweets_replied.json'

        cinema_tweets = []
        user_tweets = []
        reply_time = datetime.timedelta(seconds=0)

        with open(filename_cinema) as f:
            for line in f:
                tweet = json.loads(line)
                cinema_tweets.append(tweet)
        with open(filename_user) as f:
            for line in f:
                tweet = json.loads(line)
                user_tweets.append(tweet)

        for tweet_user in user_tweets:
            tweet_created_at = datetime.datetime.strptime(tweet_user['created_at'], '%a %b %d %H:%M:%S %z %Y')
            
            for tweet_cinema in cinema_tweets:
                if tweet_cinema['in_reply_to_status_id'] == tweet_user['id']:
                    reply_created_at = datetime.datetime.strptime(tweet_cinema['created_at'], '%a %b %d %H:%M:%S %z %Y')
            
            reply_time += (reply_created_at - tweet_created_at)

        time = math.floor(reply_time.total_seconds()/60/60/len(user_tweets))
        avg_response_time.append(time)
        reply_count_list.append(len(user_tweets))

    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure(figsize = (10, 6))
        plt.bar(cinemas, avg_response_time)
        plt.xlabel('Cinema')
        plt.ylabel('Average response time (hour)')
        plt.title('Average response time (hours) for Cinemas')
        st.pyplot(fig)
    with cols[1]:
        for i in range(3):
            st.info(cinemas[i]+' average replied in '+str(avg_response_time[i])+' hours for '+str(reply_count_list[i])+' tweets')
        st.write('TGV took the least time which is only 5 hours to respond or answer the users when being mentioned. The second fastest responding cinema is GSC which took 10 hours to respond. MMC has the poorest responsiveness towards the questions from the users. It tooks 16 hours to answer only one tweet. Meanwhile for GSC and TGV, they took less than 16 hours to respond to over 100 tweets which is far more responsive than MMC. ')

############Q4############
elif question == aspects[3]:
    st.header("4. Engagement rate (likes, retweets)")

    gsc_followers_count_data = pd.read_json('Collected_data/GSC_followers_count.json', lines=True)
    tgv_followers_count_data = pd.read_json('Collected_data/TGV_followers_count.json', lines=True)
    mmc_followers_count_data = pd.read_json('Collected_data/MMC_followers_count.json', lines=True)

    eng_rate = []

    for cinema in cinemas:
        filename = 'Collected_data/'+cinema+'_tweets.json'
        favCount = retweetCount = total_tweet = 0

        if cinema == 'GSC':
            followers_count = gsc_followers_count_data['followers_count'].values[-1]
        elif cinema == 'TGV':
            followers_count = tgv_followers_count_data['followers_count'].values[-1]
        elif cinema == 'MMC':
            followers_count = mmc_followers_count_data['followers_count'].values[-1]

        with open(filename) as f:
            for line in f:
                tweet = json.loads(line)

                if tweet['in_reply_to_status_id'] == None: #self tweet or retweet, not reply
                    total_tweet += 1
                    favCount += tweet['favorite_count']
                    retweetCount += tweet['retweet_count']

        engagement = (favCount + retweetCount) / total_tweet / followers_count * 100
        eng_rate.append(engagement)

    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure(figsize = (10, 6))
        plt.bar(cinemas, eng_rate)
        plt.xlabel('Cinema')
        plt.ylabel('Engagement rate (%)')
        plt.title('Engagement rate by Cinemas')
        st.pyplot(fig)
    with cols[1]:
        st.write('From the bar chart shown, we can tell that TGV has the highest engagement rate which is 0.3%. GSC has an engagement rate of around 0.12% and MMC has the lowest engagement rate of only 0.04%. ')

############Q5############
elif question == aspects[4]:

    st.header("5. Top 5 hashtags used")

    df_list = []

    def getTags(tweet):
        entity = tweet.get('entities',{})
        ht = entity.get('hashtags',[])
        return [tag['text'] for tag in ht]

    for cinema in cinemas:
        tag_name = []
        tag_count = []
        htags = Counter()

        filename = 'Collected_data/'+cinema+'_tweets.json'

        with open(filename) as f:
            for line in f:
                tweet = json.loads(line)
                if tweet['in_reply_to_status_id'] == None:
                    htags.update(getTags(tweet))

        for tag, count in htags.most_common(5):
            print(tag,count)
            tag_name.append(tag)
            tag_count.append(count)

        df_list.append(pd.DataFrame({'Tags':tag_name,'Tag Count':tag_count}))

    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            fig = plt.figure(figsize = (10, 6))
            plt.bar(df_list[i]['Tags'], df_list[i]['Tag Count'])
            plt.xlabel('\nTags')
            plt.ylabel('Tag Count')
            plt.yticks(range(0,21,2))
            plt.title(cinemas[i]+' Top 5 Hastags')
            st.pyplot(fig)

    st.write('From the top 5 hashtags used for each of the cinema, we can tell that GSC and TGV used the most hashtags to promote some popular and mainstream movies such as The Batman and Jujutsu Kaisen. TGV used the most hashtags which is 18 hashtags to promote the Jujutsu Kaisen movie. This is a famous anime movie, so by using more hashtags TGV increases the chance of their tweets being exposed, viewed or searched by the users. However, GSC and MMC did not use many hashtags in their tweets. MMC used 7 hashtags for Sonic Movie 2 but it is not a movie that will interest most people. ')

elif question == aspects[5]:
    follow_two_df = pd.read_csv('Collected_data/follows_two.csv')
    follow_three_df = pd.read_csv('Collected_data/follows_three.csv')
    x = ['Accounts That Follow 2 Brands', 'Accounts That Follow 3 Brands']
    
    st.header("Comparison of Average Followers Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [follow_two_df['followers_count'].mean(), follow_three_df['followers_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Followers Counts')
        plt.xlabel("Aspect")
        plt.ylabel("Average Followers Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('From the bar graph above, we can observe that the average followers count is higher for accounts that follow 3 brands as compared to the accounts that follow 2 brands. From this observation, we can assume that accounts that follow 3 brands are spending more time on social media, therefore gathering a bigger number of average follower count. Accounts that follow 3 brands are also more likely to follow more brands of other sectors on social media thus winding them up with more average followers counts.')

    st.header("Comparison of Average Friends Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [follow_two_df['friends_count'].mean(), follow_three_df['friends_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Friends Counts')
        plt.xlabel("Aspect")
        plt.ylabel("Average Friends Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('For the bar graph above, it is observed that accounts that follow 3 brands have a higher number of average friends count as compared to accounts that follow 2 brands. As mentioned before, accounts that follow more brands tend to be more active on social media. With this reasoning, it is safe to say that the accounts that follow 2 brands are less likely to be active accounts and therefore resulting in a lower average friends count.')

    st.header("Comparison of Average Statuses Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [follow_two_df['statuses_count'].mean(), follow_three_df['statuses_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Statuses Counts')
        plt.xlabel("Aspect")
        plt.ylabel("Average Statuses Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('The bar graph above shows that accounts that follow 3 brands have a higher average statuses count than accounts that follow 2 brands. We can assume that accounts that follow 3 brands are more likely to be more active as compared to accounts that follow 2 brands and are more likely to express their opinions and update their status. Also, accounts that follow 3 brands have a higher chance to be corporate brand accounts or public figure accounts that constantly post announcements and advertisements on social media platforms, therefore explaining the higher average count of statuses.')
        
    st.header("Comparison of Average Favourites Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [follow_two_df['favourites_count'].mean(), follow_three_df['favourites_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Favourites Counts')
        plt.xlabel("Aspect")
        plt.ylabel("Average Favourites Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('According to the bar graph, we can see that accounts that follow 3 brands have a higher average favorite count than accounts that follow 2 brands. It can be said that accounts with higher favorites count are more active on social media and thus have more interaction with others which lead to high  favorite count of the account. They tend to follow more accounts to have more exposure on the latest update on social media. It can also be said that accounts that follow more brands, which is “accounts that follow 3 brands” in this case have a higher chance to be public figure accounts. Public figure accounts, for example, influencers usually hold a huge pool of followers therefore they will have a higher average favorite count.')

    st.header("Comparison of Percentage Of Protected Accounts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [follow_two_df['protected'].value_counts()[1] / follow_two_df['protected'].value_counts()[0], follow_three_df['protected'].value_counts()[1] / follow_three_df['protected'].value_counts()[0]]
        ax.bar(x,y)
        plt.title('Comparison of Percentage Of Protected Accounts')
        plt.xlabel("Aspect")
        plt.ylabel("Percentage of Protected Accounts")
        st.pyplot(fig)
    with cols[1]:
        st.write('From the bar graph above, we can see that accounts that follow 2 brands have a higher percentage of protected accounts as compared to accounts that follow 3 brands. From the graph we can assume that accounts that follow 3 brands are more likely to be corporate with personal accounts, corporate brand accounts, public figure accounts, etc. Meanwhile, accounts that follow 2 brands are more likely to be pure personal accounts whereby most accounts are protected. Most pure personal accounts are more likely to be protected accounts to secure themselves from threats or unwanted attention on social media.')

elif question == aspects[6]:
    class0_df = pd.read_csv('Collected_data/communities_class0.csv')
    class1_df = pd.read_csv('Collected_data/communities_class1.csv')
    class2_df = pd.read_csv('Collected_data/communities_class2.csv')
    x = ['Class 0', 'Class 1', 'Class 2']

    st.header("Comparison of Average Followers Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [class0_df['followers_count'].mean(), class1_df['followers_count'].mean(), class2_df['followers_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Followers Counts')
        plt.xlabel("Classes")
        plt.ylabel("Average Followers Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('We can observe that Class 2 contains the highest number of average followers with the number of approximately 450, followed by Class 0 with a number of approximately 300, followed by Class 1 with the lowest number of approximately 180. Following our previous findings, MMCineplex is categorized in Class 2 but at the same time MMCineplex contains the lowest overall follower and following numbers and the lowest activity rate. The finding regarding comparison of average followers count is contradicting with the overall analysis of MMCineplex. To conclude, the average followers count is not the similarity within the community.')

    st.header("Comparison of Average Friends Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [class0_df['friends_count'].mean(), class1_df['friends_count'].mean(), class2_df['friends_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Friends Counts')
        plt.xlabel("Classes")
        plt.ylabel("Average Friends Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('For comparison of average friends counts, Class 2 is significantly higher than both Class 1 and Class 0 with the average friends counts of approximately 700, 300, and 290 respectively. Having MMCineplex categorized in Class 2, it is inaccurate to relate the comparisons to our previous findings. TGV holds the largest number of friends on their social media account followed by GSC and MMCineplex respectively. Since, MMCineplex has the lowest activity rate and the lowest friends count. To summarize, the average friends count is not the similarity within the community as well.')

    st.header("Comparison of Average Statuses Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [class0_df['statuses_count'].mean(), class1_df['statuses_count'].mean(), class2_df['statuses_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Statuses Counts')
        plt.xlabel("Classes")
        plt.ylabel("Average Statuses Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('Moving on to the comparison of average statuses counts. Class 0 which contains TGV has a number of approximately 8000, Class 1 which contains GSC has a number of approximately 4000, and Class 2 which contains MMCineplax has a number of approximately 6800 average statuses counts. Among all 3 brands, TGV has the highest activity rate which satisfies the comparison. However, Class 1 which contains GSC should have a higher number than Class 2 which contains MMCineplex. Therefore, average statuses count is not the similarity within the community as well.')
        
    st.header("Comparison of Average Favourites Counts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [class0_df['favourites_count'].mean(), class1_df['favourites_count'].mean(), class2_df['favourites_count'].mean()]
        ax.bar(x,y)
        plt.title('Comparison of Average Favourites Counts')
        plt.xlabel("Classes")
        plt.ylabel("Average Favourites Count")
        st.pyplot(fig)
    with cols[1]:
        st.write('From the bar graph above, we can observe that Class 0, Class 1, and Class 2 have at least approximately 4000 thousand average favorites count. With Class 0 having the highest number of approximately 9000, and Class 1 having a number of approximately 5800 and Class 2 having the lowest number of approximately 4000 of average favorites counts, it can be assumed that the average favorite counts does not directly relate to the amount of followers on the brands’ social media account. We can assume that since the social media account of GSC is created at an earlier time than TGV and they have gathered a bigger follower count. But at the same time this might result in a bigger amount of inactive followers as social media accounts created at an earlier period may be abandoned and turned inactive. The same goes for MMCineplex which holds the lowest number of both following and followers. The account is inactive and has a low social activity rate therefore, MMCineplex followers tend to be inactive as well. So, it is safe to conclude that the three classes can be said as the classes that have high, medium and low followers count in this case. For example, TGV falls in Class 0 while MMC falls in Class 2.')

    st.header("Comparison of Percentage Of Protected Accounts")
    cols = st.columns(2)
    with cols[0]:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        y = [class0_df['protected'].value_counts()[1] / class0_df['protected'].value_counts()[0], class1_df['protected'].value_counts()[1] / class1_df['protected'].value_counts()[0], class2_df['protected'].value_counts()[1] / class2_df['protected'].value_counts()[0]]
        ax.bar(x,y)
        plt.title('Comparison of Percentage Of Protected Accounts')
        plt.xlabel("Aspect")
        plt.ylabel("Percentage of Protected Accounts")
        st.pyplot(fig)
    with cols[1]:
        st.write('By observing the bar chart above, the comparison of percentage of protected accounts indicated that Class 0 which contains TGV has the highest percentage of approximately 0.32, followed by Class 2 which contains GSC has the percentage of approximately 0.30, and Class 1 which contains MMCineplex has the lowest percentage of approximately 0.24. We can observe that most accounts listed in Class 0 are personal accounts based on our previous findings. But unfortunately, all 3 brands are unprotected accounts thus this comparison is not related to the similarity within the community. ')
