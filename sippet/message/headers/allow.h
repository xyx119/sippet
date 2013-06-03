/* 
 * Copyright (c) 2013, Guilherme Balena Versiani
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met: 
 * 
 * 1. Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer. 
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution. 
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 * The views and conclusions contained in the software and documentation are those
 * of the authors and should not be interpreted as representing official policies, 
 * either expressed or implied, of the FreeBSD Project.
 */

#ifndef SIPPET_MESSAGE_HEADERS_ALLOW_H_
#define SIPPET_MESSAGE_HEADERS_ALLOW_H_

#include <string>
#include "sippet/message/header.h"
#include "sippet/message/headers/has_multiple.h"
#include "sippet/message/headers/has_parameters.h"
#include "sippet/base/raw_ostream.h"

namespace sippet {

class method {
public:
  method() {}
  method(const method &other) : method_(other.method_) {}
  explicit method(const std::string &meth)
    : method_(meth)
  { /* TODO: convert to upper case */ }

  ~method() {}

  method &operator=(const method &other) {
    method_ = other.method_;
    return *this;
  }

  std::string value() const { return method_; }

  void print(raw_ostream &os) const {
    os << value();
  }
private:
  std::string method_;
};

inline
raw_ostream &operator << (raw_ostream &os, const method &m) {
  m.print(os);
  return os;
}

class Allow :
  public Header,
  public has_multiple<method> {
private:
  Allow(const Allow &other) : Header(other), has_multiple(other) {}
  Allow &operator=(const Allow &);
  virtual Allow *DoClone() const {
    return new Allow(*this);
  }
public:
  Allow() : Header(Header::HDR_ALLOW) {}

  scoped_ptr<Allow> Clone() const {
    return scoped_ptr<Allow>(DoClone());
  }

  virtual void print(raw_ostream &os) const {
    os.write_hname("Allow");
    has_multiple::print(os);
  }
};

} // End of sippet namespace

#endif // SIPPET_MESSAGE_HEADERS_ALLOW_H_
