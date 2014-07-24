// Copyright (c) 2013 The Sippet Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef SIPPET_MESSAGE_HEADERS_FROM_H_
#define SIPPET_MESSAGE_HEADERS_FROM_H_

#include "sippet/message/headers/contact.h"

namespace sippet {

class From :
  public Header,
  public ContactBase,
  public has_tag<From> {
private:
  DISALLOW_ASSIGN(From);
  From(const From &other);
  virtual From *DoClone() const OVERRIDE;

public:
  From();
  From(const GURL &address, const std::string &displayName="");
  virtual ~From();

  scoped_ptr<From> Clone() const {
    return scoped_ptr<From>(DoClone());
  }

  virtual void print(raw_ostream &os) const OVERRIDE;
};

} // End of sippet namespace

#endif // SIPPET_MESSAGE_HEADERS_FROM_H_
