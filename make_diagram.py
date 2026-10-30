from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1800, 1160
img = Image.new('RGB', (W, H), '#F5F7FC')
d = ImageDraw.Draw(img)
font_regular = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font_bold = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def F(size, bold=False):
    path = font_bold if bold else font_regular
    return ImageFont.truetype(path, size)

def rounded(box, fill, outline='#DCE3F0', radius=24, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def center_text(box, text, font, fill, spacing=7):
    x1,y1,x2,y2=box
    lines=text.split('\n')
    heights=[d.textbbox((0,0), line, font=font)[3]-d.textbbox((0,0), line, font=font)[1] for line in lines]
    total=sum(heights)+spacing*(len(lines)-1)
    y=y1+(y2-y1-total)/2
    for line, h in zip(lines, heights):
        bb=d.textbbox((0,0), line, font=font)
        tw=bb[2]-bb[0]
        d.text((x1+(x2-x1-tw)/2,y),line,font=font,fill=fill)
        y += h+spacing

def label(x,y,text,fill='#66738F',font=None):
    d.text((x,y),text,font=font or F(20,True),fill=fill)

def arrow(points, color='#6678E6', width=7, head=18):
    d.line(points, fill=color, width=width, joint='curve')
    x1,y1=points[-2]; x2,y2=points[-1]
    import math
    a=math.atan2(y2-y1,x2-x1)
    p1=(x2-head*math.cos(a-0.55), y2-head*math.sin(a-0.55))
    p2=(x2-head*math.cos(a+0.55), y2-head*math.sin(a+0.55))
    d.polygon([(x2,y2),p1,p2],fill=color)

# Header
rounded((55,45,1745,205),'#1E2C83','#1E2C83',30,1)
label(95,75,'PATHWISE  /  CODE KERNEL ’26', '#C7D0FF', F(19,True))
d.text((95,112),'Adaptive learning system architecture',font=F(42,True),fill='white')
d.text((97,169),'Student-specific learning paths · Teacher-guided decisions · Learn → Solve → Test',font=F(20),fill='#D7DEFF')

# Column headers
label(85,250,'PEOPLE', '#74809A', F(17,True))
label(390,250,'APPLICATION', '#74809A', F(17,True))
label(790,250,'ADAPTATION & CONTENT', '#74809A', F(17,True))
label(1330,250,'STORAGE & INSIGHT', '#74809A', F(17,True))

# People boxes
rounded((70,300,310,475),'#FFFFFF')
center_text((90,320,290,450),'STUDENT\nClasses 6–10\nLearns, solves, tests',F(22,True),'#26345D',8)
rounded((70,700,310,875),'#FFFFFF')
center_text((90,720,290,850),'TEACHER\nReviews progress\nChooses interventions',F(22,True),'#26345D',8)

# Application layer
rounded((385,300,735,510),'#E9EDFF','#CBD3FF')
center_text((410,320,710,390),'REACT + TYPESCRIPT\nStudent interface',F(24,True),'#2E43B8',8)
center_text((410,400,710,490),'Learner profile · Topic selection\nSession progress · Feedback',F(17),'#59678A',7)

# Learning flow and decision engine
rounded((805,300,1160,510),'#FFFFFF','#D9E0EF')
center_text((830,320,1135,390),'LEARN → SOLVE → TEST',F(24,True),'#25335A',8)
center_text((830,400,1135,490),'Concept lesson · Guided practice\nCheckpoint assessment\nResponse capture',F(17),'#697590',8)
rounded((1215,300,1500,510),'#303FA9','#303FA9')
center_text((1235,320,1480,390),'ADAPTIVE RULE ENGINE',F(20,True),'#FFFFFF',8)
center_text((1235,400,1480,490),'Below 60% → revisit\n60–79% → consolidate\n80%+ → extend',F(17),'#E1E6FF',9)

# Data layer and teacher insights
rounded((1555,300,1735,510),'#FFFFFF','#D9E0EF')
center_text((1570,315,1720,390),'LOCAL\nSTORAGE',F(20,True),'#26345D',7)
center_text((1570,400,1720,490),'Mastery by topic\nActivity count\nLanguage preference',F(14),'#697590',7)
rounded((805,700,1160,910),'#F0F7FF','#D1E4FA')
center_text((830,720,1135,790),'CURRICULUM CONTENT BANK',F(20,True),'#28568A',7)
center_text((830,800,1135,890),'Sample Maths + Science\nGrade band · Prerequisite\nLessons + question bank',F(16),'#5D7898',7)
rounded((1215,700,1735,910),'#EAF8F3','#C8EBDD')
center_text((1240,720,1710,790),'TEACHER DASHBOARD & REVIEW',F(22,True),'#177A60',8)
center_text((1240,800,1710,890),'Class snapshot · Mastery bands · Learner detail\nNeeds support · Ready to advance · Suggested actions\nTeacher judgement stays central',F(16),'#4D7B70',8)

# Main horizontal flow
arrow([(310,385),(385,385)])
label(320,348,'learning activity', '#6678E6', F(13,True))
arrow([(735,405),(805,405)])
label(745,368,'opens session', '#6678E6', F(13,True))
arrow([(1160,405),(1215,405)])
label(1165,368,'performance signal', '#6678E6', F(12,True))
arrow([(1500,405),(1555,405)])
label(1505,368,'persist profile', '#6678E6', F(12,True))

# Content supplies activities; data supplies teacher insight
arrow([(982,700),(982,510)], color='#79A7D9')
label(995,590,'supplies age / topic content', '#5287BB', F(12,True))
arrow([(1645,510),(1645,700)], color='#D19A3A')
label(1658,570,'progress signals', '#B07A20', F(12,True))

# Teacher review loop routed below components to avoid obscuring system flow
arrow([(310,787),(340,787),(340,975),(1475,975),(1475,910)], color='#35A985')
label(655,945,'teacher reviews evidence and chooses the classroom intervention', '#238A6E', F(13,True))
# Footer / scope
rounded((70,1080,1725,1135),'#E9EDFA','#E9EDFA',16,1)
center_text((85,1086,1710,1128),'PROTOTYPE SCOPE: React + TypeScript · rule-based adaptation · localStorage · sample English content · no backend or multi-device sync',F(16,True),'#5A6688',4)

out=Path('/mnt/data/pathwise/architecture.png')
img.save(out,quality=95)
img.save('/mnt/data/PathWise_Architecture.png',quality=95)
print(out, img.size)
