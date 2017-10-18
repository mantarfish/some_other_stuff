var web_torrent = require('webtorrent')

var client = new WebTorrent()
var murl = 'magnet:?xt=urn:btih:d00f407f5895a855ee50d857e44fa7f73387d862&dn=american.crime.s03e02.720p.webrip.hevc.x265.rmteam.mkv&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969'


client.add(murl, funtion (torrent) {
  console.log('Client is downloading:', torrent.infoHash)

  torrent.files.forEach(funtion(file) {
    file.appendTo('body')
  }

}
