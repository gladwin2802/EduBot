import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
text = """
Ratan Tata is a shining example of success. He is a renowned Indian industrialist, investor, philanthropist, and former chairman of Tata Sons. Born in 1937, Ratan Tata has achieved remarkable success in his career. He has been credited with transforming the Tata Group, one of India's largest conglomerates, into a global powerhouse.

Ratan Tata's success story is truly inspiring. He began his career in 1962, joining the Tata Group as an apprentice. Over the years, he rose through the ranks and eventually became the chairman of Tata Sons in 1991. Under his leadership, the Tata Group grew exponentially, with its revenues increasing from $5 billion to $100 billion. He also spearheaded the acquisition of several iconic companies, such as Jaguar Land Rover and Corus Steel.

In addition to his business acumen, Ratan Tata is also known for his philanthropic endeavors. He has contributed billions of dollars to charitable causes, including education, disaster relief, and healthcare. He has also established the Tata Trusts, which are dedicated to improving the lives of the underprivileged in India. 

The success story of Ratan Tata is truly remarkable. He has achieved tremendous success in business, while also making a positive impact on society. His inspiring journey serves as a reminder that hard work and dedication can lead to great success.

The early life of Ratan Tata was one of privilege and opportunity. Born into a prominent Indian family in 1937, Ratan was exposed to the world of business from a young age. His grandfather, Jamsetji Tata, was a pioneering industrialist who founded the Tata Group, one of India's largest and most influential conglomerates. 

Ratan was raised in Mumbai and attended the prestigious Cathedral and John Connon School. He then went ahead to study architecture and structural engineering at Cornell University in the States. He gained his management degree from one of the most prestigious Ivy League “ Harvard University” after completing his architecture and structural engineering program. 

Ratan's father, Naval Tata, was adopted by Jamsetji and went on to become the chairman of the Tata Group. Ratan Tata, although, born into one of the wealthiest business families in India, the Tata Group, contributed majorly to the industrialization of India after gaining independence and despite being the heir and future chairperson of Tata Group, he showed humility and determination to learn by starting his career as an apprentice in the Tata Steel Division. 

Later in 1971, he was appointed Director-in-Charge of the National Radio and Electronics Company Limited (NELCO) when it was on the verge of shutting down and he turned the situation around positively. 

Throughout his life, Ratan Tata has been a leader in the business world, using his knowledge and experience to shape the future of the Tata Group. His early life has contributed a lot to the biography of Ratan Tata and provided him with the resources and education necessary to become a successful entrepreneur and philanthropist. 

Ratan Tata is known for his pro-activeness and futuristic approach which led him to initiate several reforms to modernize the business operations of the Tata Group when he took the leadership role in 1990 in order to remain relevant and competitive in the dynamic business environment. He started his journey by merging all Tata firms and taking over reputed companies like Tetley, and Jaguar Land Rover, and floated Tata Motors on the New York Stock Exchange, earning international recognition. 

He has been credited with transforming the Tata Group into a global conglomerate, with a presence in more than 100 countries. He has also been instrumental in launching several innovative products and services, such as the Tata Nano car and the Tata Sky satellite television service. 

Ratan Naval Tata graced the position of chairman of the Tata Group until his retirement in 2012 but he also served in 2017 as temporary chairman. During his reign in 2004, TCS ( Tata Consultancy Services), an IT services business went public, and Tata’s contribution to India’s vehicle industry has been one of its kind business moves that completely changed the perspective of luxury in the eyes of Indian consumers by building a true-blue Indian brand- the Indica and Nano. 

Ratan Tata initiated an acquisition with Ford executives as well to sell the Tata Group’s vehicle division, though, it wasn’t successful but Tata didn’t stop there. However, nine years later, Tata was able to secure Ford’s, Jaguar Land Rover purchase at a whopping price of more than $2 billion.
Ratan Tata's immense contribution to society has been nothing short of remarkable. He has been a driving force in the development of India's economy, spearheading initiatives that have improved the lives of millions of people. 

His philanthropic efforts have been far-reaching, from providing access to clean water and sanitation to supporting education and healthcare. He has also been a major advocate for environmental sustainability, investing in renewable energy sources and advocating for the conservation of natural resources. His commitment to social justice and equality has been unwavering. Thus, Ratan Tata’s contribution to society is enormous. 

The Tata Group under the leadership of Ratan Tata helped the University of New South Wales Faculty of Engineering provide a better quality water supply to unprivileged communities. 

The Tata Education and Development Trust developed Tata Scholarship Fund for Indian undergraduate students to provide them with financial help to study at Cornell University which assists around 20 students yearly to make their dream to study abroad true. 

Tata Consultancy Services (TCS) has invested $35 million in Carnegie Mellon University (CMU) for cognitive systems and an autonomous vehicle research lab which is 48,000 sq. ft. structure and is popularly known as TCS Hall making it, the greatest corporate contribution ever. 

Tata Group and Tata charities contributed $50 million to build an executive center in 2010 at Harvard Business school. 

The Indian Institute of Technology (IIT-Bombay), received the greatest grant in its history from the Tata Group (₹950 million), for establishing the Tata Center for Technology and Design (TCTD) in 2014.
Ratan Tata's immense contribution to society has been nothing short of remarkable. He has been a driving force in the development of India's economy, spearheading initiatives that have improved the lives of millions of people. 

His philanthropic efforts have been far-reaching, from providing access to clean water and sanitation to supporting education and healthcare. He has also been a major advocate for environmental sustainability, investing in renewable energy sources and advocating for the conservation of natural resources. His commitment to social justice and equality has been unwavering. Thus, Ratan Tata’s contribution to society is enormous. 

The Tata Group under the leadership of Ratan Tata helped the University of New South Wales Faculty of Engineering provide a better quality water supply to unprivileged communities. 

The Tata Education and Development Trust developed Tata Scholarship Fund for Indian undergraduate students to provide them with financial help to study at Cornell University which assists around 20 students yearly to make their dream to study abroad true. 

Tata Consultancy Services (TCS) has invested $35 million in Carnegie Mellon University (CMU) for cognitive systems and an autonomous vehicle research lab which is 48,000 sq. ft. structure and is popularly known as TCS Hall making it, the greatest corporate contribution ever. 

Tata Group and Tata charities contributed $50 million to build an executive center in 2010 at Harvard Business school. 

The Indian Institute of Technology (IIT-Bombay), received the greatest grant in its history from the Tata Group (₹950 million), for establishing the Tata Center for Technology and Design (TCTD) in 2014.
Ratan Tata was made chairman of the Tata group in 1991 when his mentor JRD decided to step down. The handover was not without its own share of issues as many others were also vying for the post. Some of them pointed to his relative inexperience to buttress their own case. However, JRD Tata stuck to his prodigy who went on to prove that he was worthy of the trust.

Ratan Tata expanded the reach of the Tata empire much beyond India, especially with some of India’s biggest ever overseas acquisitions – Jaguar Land Rover, Corus Steel and Tetley Tea. In fact, the Tata Group has now emerged as the largest employer in the UK. 

He is also the idea behind the world’s cheapest car – Tata Nano, which was less of a business and more about Ratan Tata trying to give a cheap alternative to two-wheeler owners.

By the time he left chairmanship of Tata Sons, the group’s revenue had grown over 40 times and the bottomline over 50 times. The group’s revenue totaled more than $100 billion in 2011-12, when he retired.

But his boardroom battles days were not over. His successor, Cyrus Mistry, did not get along with the Tatas on many business issues and the two sides got into a protracted legal battle. Eventually, Cyrus Mistry was asked to leave the chairmanship of Tata Sons and Tata group companies.

Mistry, who died in a road accident last year, was succeeded by Natarajan Chandrasekaran, who previously led Tata Consultancy Services.

Ratan Tata has stayed away from an active role in the group after Chandrasekaran’s appointment but has turned out to be a prolific angel investor, putting his money in many startups including Ola Electric, Paytm and Zivame.

Ratan Tata studied at Cornell and Harvard universities and started his career by working in the textile divisions of the Tata group. After learning the ropes of the business and showing his potential as a leader, he was given the responsibility of managing the overseas operations of the computer and hotel businesses. It was here that his talent got noticed. In 1991, JRD Tata chose him as his successor despite strong opposition by the senior executives in the company. From 1991 to 2012, Ratan Tata grew the Tata group from Rs. 10,000 cr to Rs. 130,000 cr, added 3 more companies and acquired reputed foreign companies. Tata Steel acquired European steel major, Corus, which was a bigger company than itself. Tata motors acquired Jaguar Land Rover which is a reputed British company which makes luxury cars. Also, Ratan Tata is responsible for making the cheapest car in the world at $2500, a feat that none of the established companies have been able to accomplish even till now. Ratan Tata was a magical leader for the company. He integrated the loosely tied and diversified companies together.

His contribution to the world leaves me both amazed and awed. Firstly, I am amazed by how charismatic he is. He worked actively till the age of 75 years before retiring from active service. Even after retiring, he helps the company with his valuable inputs. There are hardly any people his age who are as active as him. Second, I am a big fan of his philanthropic efforts. Even though he was a very ruthless

 

businessman, he never forgets to give back to the society. Two-thirds of the Tata group is owned by philanthropic groups. After retirement, he plans to work a lot more for charity. Thirdly, I would like to acquire business acumen as good as him. He paid a lot of emphasis on innovation and this helped him grow the business. His cheapest car in the world project was a revolutionary project. Even though the car hasn’t become an instant success, it will surely live up to expectations. It is commendable how despite being a relatively new automobile company, Tata motors was able to achieve what established companies have not been able to accomplish even till now. Another thing that he paid a lot of emphasis on was fore sightedness and showed how to run a successful enterprise.

"""
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text for token in doc]

punctuation = punctuation + '\n'

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                

max_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency


sentence_tokens = [sent for sent in doc.sents]

sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
                
sentence_scores
from heapq import nlargest
select_length = int(len(sentence_tokens)*0.3)
select_length
summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
summary
final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
print(summary)
print(len(text))
print(len(summary))
