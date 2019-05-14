# -*- coding: utf-8 -*-

class MarjorityVoting(object):
    
    labels = []
    votes = None
    
    def counting_votes(self, votes):
        cluster = 0
        count_vote = 0
        for vote in votes:
            if count_vote == 0:
                cluster = vote
            if vote == cluster:
                count_vote += 1
            else:
                count_vote -= 1
        return cluster
    
    def marjorityvoting(self):
        self.labels.append(self.counting_votes)
    
