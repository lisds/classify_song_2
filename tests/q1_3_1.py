test = {
  'name': 'Question 1.3.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> r = np.count_nonzero(test_guesses == test_lyrics['Genre']) / len(test_lyrics)
          >>> proportion_correct == r
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
