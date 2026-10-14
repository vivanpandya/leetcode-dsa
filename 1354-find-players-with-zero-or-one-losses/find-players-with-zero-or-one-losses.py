class Solution:
    def findWinners(self, matches):
        losses = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)

            losses[loser] = losses.get(loser, 0) + 1

        zero_losses = []
        one_loss = []

        for player in players:
            loss_count = losses.get(player, 0)

            if loss_count == 0:
                zero_losses.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        zero_losses.sort()
        one_loss.sort()

        return[zero_losses, one_loss]
