from ..db import db, Voters, Votes


def add_record(student_id, classnum, votes):
    voter = Voters(student_id, classnum)
    old_voter = Voters.query.filter_by(student_id=student_id, classnum=classnum)
    if old_voter.first():
        for i in range(1, 9):
            Votes.query.filter_by(voter_id=old_voter.first().ID, category_id=i).update({"choice": votes[i-1][i]})
    else:
        new_votes = [Votes(student_id, i + 1, vote[i + 1]) for i, vote in enumerate(votes)]
        voter.votes.extend(new_votes)
        db.session.add(voter)
    db.session.commit()
