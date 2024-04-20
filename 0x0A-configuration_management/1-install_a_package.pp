#!/usr/bin/env bash
# Install an especific version of flask (2.1.0)

package {'flask':
  provider  =>  'pip3',
  ensure  =>  '2.1.1'
}
