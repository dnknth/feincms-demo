/* global ContentEditor, django */
;(function($) {
  $(document).on('content-editor:ready', function() {
    var buttons = [
      ['_anchor', '<i class="fa fa-anchor"></i>'],
      ['_richtext', '<i class="fa fa-pencil-square-o"></i>'],
      ['_image', '<i class="fa fa-image"></i>'],
      ['_file', '<i class="fa fa-file"></i>'],
      ['_download', '<i class="fa fa-download"></i>'],
      ['_external', '<i class="fa fa-film"></i>'],
      ['_html', '<i class="fa fa-code"></i>'],

      ['_gallery', '<i class="fa fa-images"></i>'],
      ['_slide', '<i class="fa fa-image"></i>'],
      ['_snippet', '<i class="fa fa-cog"></i>'],
      ['_table', '<i class="fa fa-table"></i>'],
      ['_team', '<i class="fa fa-users"></i>'],
    ]

    for (var i = 0; i < buttons.length; ++i) {
      ContentEditor.addPluginButton('pages' + buttons[i][0], buttons[i][1])
      ContentEditor.addPluginButton('articles' + buttons[i][0], buttons[i][1])
    }
  })
})(django.jQuery)
