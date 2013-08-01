# Copyright (c) 2013 The Sippet Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'includes': [
    '../build/win_precompile.gypi',
  ],
  'targets': [
    {
      'target_name': 'sippet',
      'type': 'static_library',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '<(DEPTH)/third_party',
      ],
      'sources': [
        'base/casting.h',
        'base/format.h',
        'base/ilist.h',
        'base/ilist_node.h',
        'base/raw_ostream.cc',
        'base/raw_ostream.h',
        'base/stl_extras.h',
        'base/string_extras.h',
        'base/type_traits.h',
        'message/atom.h',
        'message/header.h',
        'message/header.cc',
        'message/headers.h',
        'message/headers/accept_encoding.h',
        'message/headers/accept.h',
        'message/headers/accept_language.h',
        'message/headers/alert_info.h',
        'message/headers/allow.h',
        'message/headers/authentication_info.h',
        'message/headers/authorization.h',
        'message/headers/call_id.h',
        'message/headers/call_info.h',
        'message/headers/contact.h',
        'message/headers/content_disposition.h',
        'message/headers/content_encoding.h',
        'message/headers/content_language.h',
        'message/headers/content_length.h',
        'message/headers/content_type.h',
        'message/headers/cseq.h',
        'message/headers/date.h',
        'message/headers/error_info.h',
        'message/headers/expires.h',
        'message/headers/from.h',
        'message/headers/generic.h',
        'message/headers/in_reply_to.h',
        'message/headers/max_forwards.h',
        'message/headers/mime_version.h',
        'message/headers/min_expires.h',
        'message/headers/organization.h',
        'message/headers/priority.h',
        'message/headers/proxy_authenticate.h',
        'message/headers/proxy_authorization.h',
        'message/headers/proxy_require.h',
        'message/headers/record_route.h',
        'message/headers/reply_to.h',
        'message/headers/require.h',
        'message/headers/retry_after.h',
        'message/headers/route.h',
        'message/headers/server.h',
        'message/headers/subject.h',
        'message/headers/supported.h',
        'message/headers/timestamp.h',
        'message/headers/to.h',
        'message/headers/unsupported.h',
        'message/headers/user_agent.h',
        'message/headers/via.h',
        'message/headers/warning.h',
        'message/headers/www_authenticate.h',
        'message/headers/bits/auth_setters.h',
        'message/headers/bits/has_auth_params.h',
        'message/headers/bits/has_multiple.h',
        'message/headers/bits/has_parameters.h',
        'message/headers/bits/param_setters.h',
        'message/headers/bits/single_value.h',
        'message/known_headers.h',
        'message/known_methods.h',
        'message/known_protocols.h',
        'message/message.h',
        'message/message.cc',
        'message/method.h',
        'message/method.cc',
        'message/parser/parser.cc',
        'message/parser/tokenizer.h',
        'message/protocol.h',
        'message/protocol.cc',
        'message/request.h',
        'message/request.cc',
        'message/response.h',
        'message/version.h',
        'message/status.h',
        'message/status.cc',
        'uri/uri.h',
        'uri/uri.cc',
        'uri/uri_canon.h',
        'uri/uri_canon.cc',
        'uri/uri_canon_internal.h',
        'uri/uri_canon_internal.cc',
        'uri/uri_parse.h',
        'uri/uri_parse.cc',
        'uri/uri_util.h',
        'uri/uri_util.cc',
        'transport/end_point.h',
        'transport/end_point.cc',
        'transport/network_layer.h',
        'transport/network_layer.cc',
        'transport/branch_factory.h',
        'transport/branch_factory.cc',
        'transport/channel.h',
        'transport/sequenced_write_stream_socket.h',
        'transport/sequenced_write_stream_socket.cc',
        'transport/framed_write_stream_socket.h',
        'transport/framed_write_stream_socket.cc',
        'transport/udp_channel_factory.h',
        'transport/udp_channel_factory.h',
        'transport/tcp_channel_factory.h',
        'transport/tcp_channel_factory.h',
        'transport/tls_channel_factory.h',
        'transport/tls_channel_factory.h',
        'transport/ws_channel_factory.h',
        'transport/ws_channel_factory.h',
        'transport/transaction_factory.h',
        'transport/transaction_factory.cc',
        'transport/client_transaction_impl.h',
        'transport/client_transaction_impl.cc',
        'transport/server_transaction_impl.h',
        'transport/server_transaction_impl.cc',
        'transport/time_delta_provider.h',
        'transport/time_delta_factory.h',
        'transport/time_delta_factory.cc',
      ],
    },  # target sippet
  ],
}
