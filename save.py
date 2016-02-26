from pattern.web import URL, plaintext
import pickle
import os
import re
import glob

# this is the url that I am finding all other transcript urls from:
TOC_url = 'http://www.presidency.ucsb.edu/debates.php'
sampletranscript_url = 'http://www.presidency.ucsb.edu/ws/index.php?pid=111520'
candidates_remarks = {}

# pre-compiling with re.S so '.' inclues \n
script_pattern = re.compile('\\n([A-Z]{4,}): (.*?)(?=\\n?[A-Z]{4,})', re.S)


def save_dictionary(d, filename, folder=''):
    ''' pickles a dictionary with filename in downloads/folder/
    '''
    if not os.path.exists('downloads/' + folder):
        os.mkdir('downloads/' + folder)
    f = open('downloads/' + folder + filename, 'w')
    pickle.dump(d, f)
    f.close


def get_remarks_from_transcript(html, start='MODERATORS'):
    ''' retrieves remarks from html transcript of a debate and stores them 
        in a dictionary {candidate: [remarks]} which is returned
    '''
    candidates_remarks = {}
    plain_text = plaintext(html)
    script_tuple = script_pattern.findall(plain_text)
    for name, remark in script_tuple:
        clean_remark = re.sub('\[[^\]]+\]', '', remark.replace('\n', ' '))
        candidates_remarks[name] = candidates_remarks.get(
            name, []) + [clean_remark]
    return candidates_remarks


def save_html(url, filename, folder=''):
    ''' saves html from url to filename in downloads/folder/
    '''
    if not os.path.exists('downloads/' + folder):
        os.mkdir('downloads/' + folder)
    result = URL(url).download()
    f = open('downloads/' + folder + filename, 'w')
    f.write(result)
    f.close()


def get_transcript_links(
        html, years, end_string='Candidates Debate in'):
    ''' returns a list of debate transcript links retrieved from html
        (the table of contents page)
    '''
    if isinstance(years, int):
        years = (years,)

    year_pattern = '(?:'+'|'.join(str(year) for year in years)+')'

    url_pattern = re.compile(
        ', {0}.{1}href="(http:\/\/[^"]*?)">(?:Republican|Democratic)'.format(
            year_pattern, '{10,200}?'),
        re.S)
    links = re.findall(
        url_pattern,
        html)
    return [link for link in links if link]


def get_html_transcripts():
    ''' saves html retrieved from links found on table of contents page
    '''
    print 'getting table of contents...'
    # TOC_html = URL(TOC_url).download()
    TOC_html = open('downloads/index.html', 'r').read()

    links = get_transcript_links(TOC_html, (2015, 2016))
    print 'downloading html transcripts...'
    # print links
    for link in links:
        save_html(link, 'script' +
                  str(links.index(link)) +
                  '.html', 'html_transcripts/')

    print 'html is saved.'


def merge_dictionaries(dictionaries, default=[]):
    ''' returns a single list dictionary {key: [values]} which combines list
        values for all input dictionaries
    >>> merge_dictionaries({'a':[1,2], 'b':[3,4]}, {'b':[5,6], 'c':[7,8]})
    {'a': [1, 2], 'b': [3, 4, 5, 6], 'c': [7, 8]}  # or similar
    '''
    master = {}
    for d in dictionaries:
        for key in d:
            master[key] = master.get(key, default) + d[key]
    return master


def build_candidate_remarks():
    ''' compiles a master set of remarks from html transcripts merged together
        and stores it in master.pickle in downloads
    >>> build_candidate_remarks()
    '''
    project_dir = os.getcwd()

    transcript_paths = glob.glob(project_dir+'/downloads/html_transcripts/*')

    # this block is legacy--saves individual debate dictionaries before
    # merge to master:

    # debate_no = 0
    # for html_transcript in transcript_paths:
    #     transcript = open(html_transcript, 'r').read()
    #     d = get_remarks_from_transcript(transcript)
    #     save_dictionary(d, 'script{}.pickle'.format(debate_no), 'data/')
    #     debate_no += 1

    print 'getting debate remarks dictionaries...'
    debate_dictionaries = [
        get_remarks_from_transcript(
            open(html_transcript, 'r').read()
            )
        for html_transcript in transcript_paths
        ]

    print 'merging dictionaries...'
    master = merge_dictionaries(debate_dictionaries)

    print 'pickling and saving...'
    save_dictionary(master, 'master.pickle', 'data/')

    print 'master remarks dictionary saved'


if __name__ == '__main__':

    build_candidate_remarks()
    # import doctest
    # doctest.run_docstring_examples(
    #     build_candidate_remarks, globals(), verbose=True, name="Jus' Testin'")
