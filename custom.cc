#include "tensorflow/core/framework/resource_mgr.h"
#include "tensorflow/core/framework/resource_op_kernel.h"

namespace {

using namespace tensorflow;

class Search : public ResourceBase {};

REGISTER_RESOURCE_HANDLE_OP(Search);
REGISTER_RESOURCE_HANDLE_KERNEL(Search);

}  // namespace
