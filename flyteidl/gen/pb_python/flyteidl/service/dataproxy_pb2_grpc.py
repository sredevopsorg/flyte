# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from flyteidl.service import dataproxy_pb2 as flyteidl_dot_service_dot_dataproxy__pb2


class DataProxyServiceStub(object):
  """DataProxyService defines an RPC Service that allows access to user-data in a controlled manner.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateUploadLocation = channel.unary_unary(
        '/flyteidl.service.DataProxyService/CreateUploadLocation',
        request_serializer=flyteidl_dot_service_dot_dataproxy__pb2.CreateUploadLocationRequest.SerializeToString,
        response_deserializer=flyteidl_dot_service_dot_dataproxy__pb2.CreateUploadLocationResponse.FromString,
        )


class DataProxyServiceServicer(object):
  """DataProxyService defines an RPC Service that allows access to user-data in a controlled manner.
  """

  def CreateUploadLocation(self, request, context):
    """CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataProxyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateUploadLocation': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUploadLocation,
          request_deserializer=flyteidl_dot_service_dot_dataproxy__pb2.CreateUploadLocationRequest.FromString,
          response_serializer=flyteidl_dot_service_dot_dataproxy__pb2.CreateUploadLocationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'flyteidl.service.DataProxyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
