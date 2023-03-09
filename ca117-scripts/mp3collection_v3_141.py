#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, lst=None):
        self.lst = lst
        if self.lst is None:
            self.lst = []
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nBy: {', '.join(self.lst)}\nDuration: {self.duration // 60}:{self.duration % 60:02d}"

    def add_artist(self, artist):
        self.lst.append(artist)

    def __add__(self, other):
        return self + other


class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, track):
        self.d[track.title] = track

    def remove(self, track):
        if track in self.d:
            del self.d[track]

    def lookup(self, track):
        if track in self.d:
            return self.d[track]
        else:
            return None

    def get_mp3s_by_artist(self, artist):
        tracklist = []
        for track in self.d.values():
            if artist in track.lst:
                tracklist.append(track)
        return [track for track in tracklist]

    def __add__(self, other):
        res = []
        for i in self.d.values():
            res.append(i)
        for i in other.d.values():
            res.append(i)
        for i in res:
            c = MP3Collection()
            c.add(i)
        return c
