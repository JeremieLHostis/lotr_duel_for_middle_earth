from game_engine.material.alliance_of_the_free_races.alliance_tokens_board import (
    AllianceTokensBoard,
)
from game_engine.material.battle_for_the_middle_earth.map import Map
from game_engine.material.quest_for_the_ring.ring_track import RingTrack

if __name__ == "__main__":
    ''' test basique carte '''
    print(Map())

    ''' test basique piste de l'anneau '''
    print(RingTrack())

    ''' test basique jetons d'alliance '''
    alliance_tokens = AllianceTokensBoard()
    print(alliance_tokens)