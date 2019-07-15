import matplotlib.pyplot as plt
import broadway

day = []
HamAud = []

shows = broadway.get_shows()

# print(shows)

for show in shows:
    if show["Show"]["Name"] == 'Hamilton':
        HamAud.append(show["Statistics"]["Attendance"])
        day.append(show["Date"]["Day"])


# print(HamAud)
print()

plt.scatter(day, HamAud)
plt.legend(['Hamilton'], loc = 'upper left')

plt.xlabel('Day')
plt.ylabel('Attendance')
plt.title('Attendance on Broadway')

plt.show()


# import school_scores
#
# years = []
# AL_scores = []
# MA_scores = []
#
# scores = school_scores.get_all()
#
# for score in scores:
#     if score["State"]["Code"] == 'AL':
#         AL_scores.append(score["Total"]["Math"])
#         years.append(score["Year"])
#     elif score["State"]["Code"] == 'MA':
#         MA_scores.append(score["Total"]["Math"])
#
# plt.plot(years, AL_scores)
# plt.plot(years, MA_scores)
# plt.legend(['AL', 'MA'], loc = 'upper left')
#
# plt.xlabel('Years')
# plt.ylabel('Scores')
# plt.title('Average Math SAT scores in AL and MA')
#
# plt.show()
