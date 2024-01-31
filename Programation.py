from Spot import Spot
from ListVideos import ListVideos

class Programation:
  def __init__(self, url):
    self.main(url)
    
  def main(self, url):
    lista     = ListVideos(url)
    listJson  = lista.get_listVideos()
    if listJson is not None:
      for video in listJson:
        spot = Spot(video['src'], video['solofile'], video['type'])

